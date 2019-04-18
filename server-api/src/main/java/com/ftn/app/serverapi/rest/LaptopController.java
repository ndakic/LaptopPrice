package com.ftn.app.serverapi.rest;

import com.ftn.app.serverapi.model.Laptop;
import com.ftn.app.serverapi.service.LaptopService;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.*;

import javax.validation.constraints.NotNull;
import java.util.List;


@RestController
@RequestMapping("/api/laptop")
@RequiredArgsConstructor
public class LaptopController {

    @NotNull
    private final LaptopService laptopService;

    @PostMapping("/save")
    public Laptop saveLaptop(@RequestBody Laptop laptop){
        return laptopService.saveLaptop(laptop);
    }

    @GetMapping("/{id}")
    public Laptop getLaptop(@PathVariable Long id){
        return laptopService.getLaptop(id);
    }

    @GetMapping("/all")
    public List<Laptop> getAllLaptops(){
        return laptopService.getAllLaptops();
    }

}
