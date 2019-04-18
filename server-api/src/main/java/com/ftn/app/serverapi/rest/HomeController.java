package com.ftn.app.serverapi.rest;

import com.ftn.app.serverapi.resource.ResponseResource;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api")
@RequiredArgsConstructor
public class HomeController {

    @GetMapping("/test")
    public ResponseEntity test(){
        return ResponseEntity.ok(new ResponseResource("Hello From Docker!", HttpStatus.OK.value()));
    }


}
