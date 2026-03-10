package br.edu.ifmt.mini_xsig.config;

import br.edu.ifmt.mini_xsig.model.Bolsista;
import br.edu.ifmt.mini_xsig.repository.BolsistaRepository;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class DataSeeder {

    @Bean
    CommandLineRunner initDatabase(BolsistaRepository bolsistaRepository) {
        return args -> {
            // Criando o Bolsista 1 (O nosso famoso João)
            Bolsista b1 = new Bolsista();
            b1.setNome("João da Silva");
            b1.setIra(6.8);
            b1.setStatus("BLOQUEADO");
            b1.setVinculo("CLT");
            bolsistaRepository.save(b1); // Vai salvar com ID 1

            // Criando a Bolsista 2
            Bolsista b2 = new Bolsista();
            b2.setNome("Maria Souza");
            b2.setIra(8.5);
            b2.setStatus("ATIVO");
            b2.setVinculo("NENHUM");
            bolsistaRepository.save(b2); // Vai salvar com ID 2

            System.out.println("✅ Dados falsos inseridos no banco com sucesso!");
        };
    }
}