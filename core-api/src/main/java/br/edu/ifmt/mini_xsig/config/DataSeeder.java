package br.edu.ifmt.mini_xsig.config;

import br.edu.ifmt.mini_xsig.model.Bolsista;
import br.edu.ifmt.mini_xsig.model.Edital;
import br.edu.ifmt.mini_xsig.repository.BolsistaRepository;
import br.edu.ifmt.mini_xsig.repository.EditalRepository;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.time.LocalDate;

@Configuration
public class DataSeeder {

    @Bean
    CommandLineRunner initDatabase(BolsistaRepository bolsistaRepository, EditalRepository editalRepository) {
        return args -> {
            // --- BOLSISTAS ---
            Bolsista b1 = new Bolsista();
            b1.setNome("João da Silva");
            b1.setIra(6.8);
            b1.setStatus("BLOQUEADO");
            b1.setVinculo("CLT");
            bolsistaRepository.save(b1);

            Bolsista b2 = new Bolsista();
            b2.setNome("Maria Souza");
            b2.setIra(8.5);
            b2.setStatus("ATIVO");
            b2.setVinculo("NENHUM");
            bolsistaRepository.save(b2);

            // --- EDITAIS ---
            Edital e1 = new Edital();
            e1.setNumero("01/2026");
            e1.setTitulo("Bolsa de Pesquisa Aplicada FAPEMAT");
            e1.setIraMinimo(7.0);
            e1.setPermiteClt(false);
            e1.setDataFimInscricao(LocalDate.of(2026, 5, 30));
            editalRepository.save(e1);

            Edital e2 = new Edital();
            e2.setNumero("02/2026");
            e2.setTitulo("Inovação Tecnológica e Sistemas");
            e2.setIraMinimo(6.5);
            e2.setPermiteClt(true);
            e2.setDataFimInscricao(LocalDate.of(2026, 8, 15));
            editalRepository.save(e2);

            System.out.println("✅ Dados falsos (Bolsistas e Editais) inseridos no banco com sucesso!");
        };
    }
}