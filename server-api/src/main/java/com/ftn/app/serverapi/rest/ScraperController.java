package com.ftn.app.serverapi.rest;

import com.ftn.app.serverapi.model.Laptop;
import com.ftn.app.serverapi.model.Scraper;
import com.ftn.app.serverapi.service.ScraperService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import javax.validation.constraints.NotNull;
import java.util.List;

@RestController
@RequestMapping("/api/scraper")
@RequiredArgsConstructor
public class ScraperController {

    @NotNull
    private final ScraperService getAllLaptops;

    @GetMapping("/all")
    public List<Scraper> getAll(){
        return getAllLaptops.getAll();
    }

}
