// tslint:disable: no-string-literal

import { Component, OnInit, Input, OnDestroy } from '@angular/core';
import { LaptopService } from '../laptop/services/laptop.service';
import { Laptop } from '../laptop/models/laptop';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from 'src/environments/environment';
import { BlockUI, NgBlockUI } from 'ng-block-ui';

@Component({
  selector: 'app-result',
  templateUrl: './result.component.html',
  styleUrls: ['./result.component.css']
})
export class ResultComponent implements OnInit {

  public laptop: Laptop;
  public laptopPriceKNN: any;
  public laptopPriceMLR: any;
  public laptopPriceKnnRMSE: any;
  public laptopPriceMlrRMSE: any;
  public showSimilarLaptops = false;
  public similarLaptops: any;

  @BlockUI() blockUI: NgBlockUI;

  constructor(
    public laptopService: LaptopService,
    private http: HttpClient,
  ) {
    this.laptop = new Laptop();
   }

  ngOnInit() {
    this.laptopPriceKNN = 0;
    this.laptopPriceMLR = 0;
    this.laptopPriceKnnRMSE = 0;
    this.laptopPriceMlrRMSE = 0;

    if (this.laptopService.getLaptopSpecs()) {
      this.laptop = this.laptopService.getLaptopSpecs();
      this.blockUI.start('Please wait..');
      this.getLaptopPriceKNN(this.laptop).subscribe(response => {
        this.laptopPriceKNN = response['result'];
        this.laptopPriceKnnRMSE = response['RMSE'];
        localStorage.setItem('laptopSpecs', JSON.stringify(this.laptop));
        localStorage.setItem('laptopPriceKNN', this.laptopPriceKNN.toString());
        localStorage.setItem('laptopPriceKnnRMSE', this.laptopPriceKnnRMSE.toString());
        this.blockUI.stop();
      });
      this.getLaptopPriceMLR(this.laptop).subscribe(response => {
        this.laptopPriceMLR = response['result'];
        this.laptopPriceMlrRMSE = response['RMSE'];
        localStorage.setItem('laptopSpecs', JSON.stringify(this.laptop));
        localStorage.setItem('laptopPriceMLR', this.laptopPriceMLR.toString());
        localStorage.setItem('laptopPriceMlrRMSE', this.laptopPriceMlrRMSE.toString());
      });
    } else {
      if (localStorage.getItem('laptopSpecs') !== null) {
        this.laptop = JSON.parse(localStorage.getItem('laptopSpecs'));
        this.laptopPriceKNN = localStorage.getItem('laptopPriceKNN');
        this.laptopPriceMLR = localStorage.getItem('laptopPriceMLR');
        this.laptopPriceKnnRMSE = localStorage.getItem('laptopPriceKnnRMSE');
        this.laptopPriceMlrRMSE = localStorage.getItem('laptopPriceMlrRMSE');
      }
    }
  }

  getLaptopPriceMLR(laptop) {
    const httpHeaders = new HttpHeaders({
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET,POST,PATCH,DELETE,PUT,OPTIONS',
      'Access-Control-Allow-Headers': 'Origin, Content-Type, X-Auth-Token, content-type'
    });
    return this.http.post(environment.predictionApi + '/predict-price-mlr', laptop, { headers : httpHeaders});
  }

  getLaptopPriceKNN(laptop) {
    const httpHeaders = new HttpHeaders({
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET,POST,PATCH,DELETE,PUT,OPTIONS',
      'Access-Control-Allow-Headers': 'Origin, Content-Type, X-Auth-Token, content-type'
    });
    return this.http.post(environment.predictionApi + '/predict-price-knn', laptop, { headers : httpHeaders});
  }
}
