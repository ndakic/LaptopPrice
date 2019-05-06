import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders, HttpErrorResponse } from '@angular/common/http';
import { environment } from 'src/environments/environment';
import { catchError } from 'rxjs/operators';
import { throwError, BehaviorSubject } from 'rxjs';
import { Laptop } from '../models/laptop';

@Injectable({
  providedIn: 'root'
})
export class LaptopService {

  private laptop = new BehaviorSubject(new Laptop());
  sub = this.laptop.asObservable();

  constructor(private http: HttpClient) { }

  setLaptopSpecs(laptop: Laptop) {
    this.laptop.next(laptop);
  }

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

  getLaptopBrands() {
    const httpHeaders = new HttpHeaders({
      'Content-Type': 'application/json'
    });

    return this.http.get(environment.apiUrlPrefix + '/api/laptop/all-laptop-brands', { headers: httpHeaders}).pipe
    (catchError(this.handleError));
  }

  getProcessorBrands() {
    const httpHeaders = new HttpHeaders({
      'Content-Type': 'application/json'
    });

    return this.http.get(environment.apiUrlPrefix + '/api/laptop/all-processor-brands', { headers: httpHeaders}).pipe
    (catchError(this.handleError));
  }

  getAllProcessorModels() {
    const httpHeaders = new HttpHeaders({
      'Content-Type': 'application/json'
    });

    return this.http.get(environment.apiUrlPrefix + '/api/laptop/all-processor-models', { headers: httpHeaders}).pipe
    (catchError(this.handleError));
  }

  getAllProcessorCores() {
    const httpHeaders = new HttpHeaders({
      'Content-Type': 'application/json'
    });

    return this.http.get(environment.apiUrlPrefix + '/api/laptop/all-processor-cores', { headers: httpHeaders}).pipe
    (catchError(this.handleError));
  }

  getAllRamGenerations() {
    const httpHeaders = new HttpHeaders({
      'Content-Type': 'application/json'
    });

    return this.http.get(environment.apiUrlPrefix + '/api/laptop/all-ram-generations', { headers: httpHeaders}).pipe
    (catchError(this.handleError));
  }

  getAllRamAmounts() {
    const httpHeaders = new HttpHeaders({
      'Content-Type': 'application/json'
    });

    return this.http.get(environment.apiUrlPrefix + '/api/laptop/all-ram-amounts', { headers: httpHeaders}).pipe
    (catchError(this.handleError));
  }

  getAllStorageTypes() {
    const httpHeaders = new HttpHeaders({
      'Content-Type': 'application/json'
    });

    return this.http.get(environment.apiUrlPrefix + '/api/laptop/all-storage-types', { headers: httpHeaders}).pipe
    (catchError(this.handleError));
  }

  getAllStorageAmounts() {
    const httpHeaders = new HttpHeaders({
      'Content-Type': 'application/json'
    });

    return this.http.get(environment.apiUrlPrefix + '/api/laptop/all-storage-amounts', { headers: httpHeaders}).pipe
    (catchError(this.handleError));
  }

  getAllScreenSizes() {
    const httpHeaders = new HttpHeaders({
      'Content-Type': 'application/json'
    });

    return this.http.get(environment.apiUrlPrefix + '/api/laptop/all-screen-sizes', { headers: httpHeaders}).pipe
    (catchError(this.handleError));
  }

  getAllLaptopConditions() {
    const httpHeaders = new HttpHeaders({
      'Content-Type': 'application/json'
    });

    return this.http.get(environment.apiUrlPrefix + '/api/laptop/all-conditions', { headers: httpHeaders}).pipe
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
