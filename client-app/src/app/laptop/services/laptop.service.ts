import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { environment } from 'src/environments/environment';
import { catchError } from 'rxjs/operators';
import { throwError } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class LaptopService {

  constructor(private http: HttpClient) { }

  getLaptops() {
    const httpHeaders = new HttpHeaders({
      'Content-Type': 'application/json'
    });
    
    return this.http.get(environment.apiUrlPrefix + '/api/laptop/all', { headers: httpHeaders}).pipe
    (catchError(this.handleError));
  }

  getScraperInfo() {
    const httpHeaders = new HttpHeaders({
      'Content-Type': 'application/json'
    });
    
    return this.http.get(environment.apiUrlPrefix + '/api/scraper/all', { headers: httpHeaders}).pipe
    (catchError(this.handleError));
  }


  private handleError(error: HttpErrorResponse) {
    if (error.error instanceof ErrorEvent) {
      console.log('An error occurred:', error.error.message);
    } else {
      console.error(`Backend returned code ${error.status}, body was: ${error.error}`);
    }
    return throwError('Something bad happened; please try again later.');
  }

}
