package com.ftn.app.serverapi.resource;

import lombok.*;

@Getter
@Setter
@ToString
@NoArgsConstructor
@AllArgsConstructor
public class ResponseResource {

    private String message;
    private Integer code;

}
