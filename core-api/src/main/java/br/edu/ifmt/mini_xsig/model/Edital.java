package br.edu.ifmt.mini_xsig.model;

import jakarta.persistence.*;
import lombok.Data;
import java.time.LocalDate;

@Data // O Lombok gera os Getters e Setters automaticamente (menos código sujo!)
@Entity // Avisa o Spring que esta classe vai virar uma Tabela no Banco de Dados
@Table(name = "tb_edital")
public class Edital {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String numero;
    private String titulo;
    private Double iraMinimo;
    private boolean permiteClt;
    private LocalDate dataFimInscricao;

}