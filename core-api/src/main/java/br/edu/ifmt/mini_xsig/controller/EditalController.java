package br.edu.ifmt.mini_xsig.controller;

import br.edu.ifmt.mini_xsig.model.Edital;
import br.edu.ifmt.mini_xsig.repository.EditalRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/editais")
public class EditalController {

    @Autowired
    private EditalRepository repository;

    // A IA vai usar isso para listar os editais
    @GetMapping
    public List<Edital> listarEditais() {
        return repository.findAll();
    }

    // A IA vai usar isso para criar um edital novo
    @PostMapping
    public ResponseEntity<Edital> criarEdital(@RequestBody Edital edital) {
        return ResponseEntity.ok(repository.save(edital));
    }
}