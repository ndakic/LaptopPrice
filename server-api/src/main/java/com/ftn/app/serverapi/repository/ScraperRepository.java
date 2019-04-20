package com.ftn.app.serverapi.repository;

import com.ftn.app.serverapi.model.Scraper;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ScraperRepository extends JpaRepository<Scraper, Long> {
}
