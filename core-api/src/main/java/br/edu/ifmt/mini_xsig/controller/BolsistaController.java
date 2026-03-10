package br.edu.ifmt.mini_xsig.controller;

import br.edu.ifmt.mini_xsig.model.Bolsista;
import br.edu.ifmt.mini_xsig.repository.BolsistaRepository;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/bolsistas")
public class BolsistaController {

    private final BolsistaRepository repository;

    // Injeção de dependência pelo construtor
    public BolsistaController(BolsistaRepository repository) {
        this.repository = repository;
    }

    // Endpoint: GET /api/bolsistas/{id}
    @GetMapping("/{id}")
    public ResponseEntity<Bolsista> buscarPorId(@PathVariable Long id) {
        return repository.findById(id)
                .map(bolsista -> ResponseEntity.ok().body(bolsista))
                .orElse(ResponseEntity.notFound().build());
    }

    // A IA vai usar isso para listar todos os bolsistas
    @GetMapping
    public List<Bolsista> listarTodos() {
        return repository.findAll();
    }

    // A IA vai usar isso para cadastrar um novo bolsista (e vincular ao edital)
    @PostMapping
    public ResponseEntity<Bolsista> criarBolsista(@RequestBody Bolsista bolsista) {
        Bolsista novoBolsista = repository.save(bolsista);
        return ResponseEntity.ok(novoBolsista);
    }
}