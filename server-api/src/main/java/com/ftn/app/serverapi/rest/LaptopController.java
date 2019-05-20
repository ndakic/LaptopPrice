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

    @GetMapping("/{lbound}/{ubound}/{condition}")
    public List<Laptop> getLaptopsByBrand(@PathVariable Integer lbound, @PathVariable Integer ubound, @PathVariable String condition){
        return laptopService.getAllLaptopsByPriceBoundsAndCondition(lbound, ubound, condition);
    }

    @GetMapping("/search/{term}")
    public List<Laptop> getLaptopsByBrand(@PathVariable String term){
        return laptopService.searchLaptopsByBrand(term);
    }

    @GetMapping("/all-laptop-brands")
    public List<String> getAllLaptopBrands(){
        return laptopService.getAllLaptopBrands();
    }

    @GetMapping("/all-processor-brands")
    public List<String> getAllProcessorBrands(){
        return laptopService.getAllLaptopProcessorBrands();
    }

    @GetMapping("/all-processor-models")
    public List<String> getAllProcessorModels(){
        return laptopService.getAllLaptopProcessorModels();
    }

    @GetMapping("/all-processor-cores")
    public List<String> getAllProcessorCores(){
        return laptopService.getAllLaptopCores();
    }

    @GetMapping("/all-ram-generations")
    public List<String> getAllRamGenerations(){
        return laptopService.getAllLaptopRamGenerations();
    }

    @GetMapping("/all-ram-amounts")
    public List<String> getAllRamAmounts(){
        return laptopService.getAllLaptopRamAmounts();
    }

    @GetMapping("/all-storage-types")
    public List<String> getAllStorageTypes(){
        return laptopService.getAllLaptopStorageTypes();
    }

    @GetMapping("/all-storage-amounts")
    public List<String> getAllStorageAmounts(){
        return laptopService.getAllLaptopStorageAmounts();
    }

    @GetMapping("/all-screen-sizes")
    public List<String> getAllScreenSizes(){
        return laptopService.getAllLaptopScreenSizes();
    }

    @GetMapping("/all-conditions")
    public List<String> getAllLaptopConditions(){
        return laptopService.getAllLaptopConditions();
    }

}
