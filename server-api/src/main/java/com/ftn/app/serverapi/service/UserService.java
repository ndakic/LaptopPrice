package com.ftn.app.serverapi.service;

import com.ftn.app.serverapi.model.User;
import com.ftn.app.serverapi.repository.UserRepository;
import com.ftn.app.serverapi.resource.UserResource;
import lombok.AllArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@AllArgsConstructor
public class UserService {

    private UserRepository userRepository;

    public List<User> getAllUsers(){
        return userRepository.findAll();
    }

    public User getUserByUsername(String username){
        return userRepository.getOneByUsername(username).orElse(null);
    }

    public String saveUser(UserResource userResource) {

        if(userRepository.getOneByUsername(userResource.getUsername()).isPresent()){
            return String.format("User with username %s already exist!", userResource.getUsername());
        }

        userRepository.save(User.builder().username(userResource.getUsername()).password(userResource.getPassword()).email(userResource.getEmail()).firstName(userResource.getFirstName()).lastName(userResource.getLastName()).build());

        return String.format("User with username %s successfully created!", userResource.getUsername());
    }

}
