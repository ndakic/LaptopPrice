package com.ftn.app.serverapi.repository;

import com.ftn.app.serverapi.model.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface UserRepository extends JpaRepository<User, Long> {

    Optional<User> getOneByUsername(String username);

}
