package com.ftn.app.serverapi.Util;

import com.ftn.app.serverapi.model.User;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Component;

import java.util.Date;
import java.util.concurrent.TimeUnit;

@Component
@RequiredArgsConstructor
public class JwtGenerator {

    private final String secretKey = "Hell0WorlD";

    public String generateToken(User user) {
        long expirationTime = TimeUnit.DAYS.toMillis(172800000); // 2 days

        return Jwts.builder()
                .setSubject(user.getUsername())
                .setExpiration(new Date(System.currentTimeMillis() + expirationTime))
                .signWith(SignatureAlgorithm.HS512, secretKey.getBytes())
                .compact();
    }
}
