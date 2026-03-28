package br.edu.ifmt.mini_xsig.controller;

import br.edu.ifmt.mini_xsig.model.Bolsista;
import br.edu.ifmt.mini_xsig.model.Edital;
import br.edu.ifmt.mini_xsig.repository.BolsistaRepository;
import br.edu.ifmt.mini_xsig.repository.EditalRepository;
import br.edu.ifmt.mini_xsig.dto.ErroNegocio;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;
import java.util.Optional;

@RestController
@RequestMapping("/api/editais")
public class EditalController {

    @Autowired
    private EditalRepository editalRepository;

    @Autowired
    private BolsistaRepository bolsistaRepository;

    @GetMapping
    public List<Edital> listarEditais() {
        return editalRepository.findAll();
    }

    @PostMapping
    public ResponseEntity<Edital> criarEdital(@RequestBody Edital edital) {
        return ResponseEntity.ok(editalRepository.save(edital));
    }

    @PostMapping("/vincular/{idBolsista}/{idEdital}")
    public ResponseEntity<?> vincular(@PathVariable Long idBolsista, @PathVariable Long idEdital) {
        Optional<Bolsista> bolsistaOpt = bolsistaRepository.findById(idBolsista);
        Optional<Edital> editalOpt = editalRepository.findById(idEdital);

        if (bolsistaOpt.isEmpty() || editalOpt.isEmpty()) {
            return ResponseEntity.badRequest().body(
                    new ErroNegocio("DADOS_NAO_ENCONTRADOS", "Bolsista ou Edital inexistente no sistema.")
            );
        }

        Bolsista bolsista = bolsistaOpt.get();
        Edital edital = editalOpt.get();

        if (bolsista.getIra() < edital.getIraMinimo()) {
            return ResponseEntity.badRequest().body(
                    new ErroNegocio("IRA_INSUFICIENTE", "O IRA do bolsista (" + bolsista.getIra() + ") é menor que o exigido pelo edital (" + edital.getIraMinimo() + ").")
            );
        }

        if ("BLOQUEADO".equals(bolsista.getStatus())) {
            return ResponseEntity.badRequest().body(
                    new ErroNegocio("STATUS_BLOQUEADO", "O bolsista está bloqueado e não pode assumir editais.")
            );
        }

        return ResponseEntity.ok(Map.of(
                "sucesso", true,
                "mensagem", "O vínculo foi realizado com sucesso no banco de dados."
        ));
    }
}