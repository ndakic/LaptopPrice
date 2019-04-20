package com.ftn.app.serverapi.service;

import com.ftn.app.serverapi.model.Scraper;
import com.ftn.app.serverapi.repository.ScraperRepository;
import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@AllArgsConstructor
public class ScraperService {

    private ScraperRepository scraperRepository;

    public List<Scraper> getAll(){
        return scraperRepository.findAll();
    }

}
