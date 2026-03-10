package br.edu.ifmt.mini_xsig.model;

import jakarta.persistence.*;
import lombok.Data;

@Data
@Entity
@Table(name = "tb_bolsista")
public class Bolsista {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String nome;
    private Double ira;
    private String status; // Ex: ATIVO, BLOQUEADO
    private String vinculo; // Ex: CLT, NENHUM

    // Simula a qual edital o aluno está tentando a bolsa
    @ManyToOne
    @JoinColumn(name = "edital_id")
    private Edital edital;

}