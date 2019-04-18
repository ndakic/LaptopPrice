package com.ftn.app.serverapi.resource;

import lombok.*;

@Getter
@Setter
@ToString
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class TokenResource {

    private String message;
    private Integer code;
    private String token;

}
