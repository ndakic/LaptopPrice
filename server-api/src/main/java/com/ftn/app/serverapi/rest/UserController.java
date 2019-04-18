package com.ftn.app.serverapi.rest;

import com.ftn.app.serverapi.model.User;
import com.ftn.app.serverapi.resource.ResponseResource;
import com.ftn.app.serverapi.resource.UserResource;
import com.ftn.app.serverapi.service.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.validation.constraints.NotNull;
import java.util.List;

@RestController
@RequestMapping("/api/user")
@RequiredArgsConstructor
public class UserController {

    @NotNull
    private final UserService userService;

    @PostMapping("/save")
    public ResponseEntity saveUser(@RequestBody UserResource userResource){
        return ResponseEntity.ok(new ResponseResource(userService.saveUser(userResource), HttpStatus.OK.value()));
    }

    @GetMapping("/{username}")
    public User getUsers(@PathVariable String username){
        return userService.getUserByUsername(username);
    }

    @GetMapping("/all")
    public List<User> getUsers(){
        return userService.getAllUsers();
    }

}
