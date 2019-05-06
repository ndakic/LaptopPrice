import { Component, OnInit, Input, OnDestroy } from '@angular/core';
import { LaptopService } from '../laptop/services/laptop.service';
import { Laptop } from '../laptop/models/laptop';

@Component({
  selector: 'app-result',
  templateUrl: './result.component.html',
  styleUrls: ['./result.component.css']
})
export class ResultComponent implements OnInit, OnDestroy {

  public laptop: Laptop;

  constructor(
    public laptopService: LaptopService
  ) {
    this.laptop = new Laptop();
   }

  ngOnInit() {

    if (localStorage.getItem('laptop') !== null) {
      this.laptop = JSON.parse(localStorage.getItem('laptop'));
    }

    this.laptopService.sub.subscribe(laptop => {
      if (laptop.laptopBrand) {
        this.laptop = laptop;
      }
      if (localStorage.getItem('laptop') === null) {
        localStorage.setItem('laptop', JSON.stringify(this.laptop));
      }
    });
  }

  ngOnDestroy() {
    localStorage.removeItem('laptop');
  }
}

