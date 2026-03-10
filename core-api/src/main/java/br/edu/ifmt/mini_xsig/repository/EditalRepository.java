package br.edu.ifmt.mini_xsig.repository;

import br.edu.ifmt.mini_xsig.model.Edital;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface EditalRepository extends JpaRepository<Edital, Long> {
}