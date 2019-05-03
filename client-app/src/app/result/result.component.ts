import { Component, OnInit, Input } from '@angular/core';

@Component({
  selector: 'app-result',
  templateUrl: './result.component.html',
  styleUrls: ['./result.component.css']
})
export class ResultComponent implements OnInit {

  public laptop: any;

  constructor() { }

  ngOnInit() {

    this.laptop = {
      laptopBrand : 'Asus',
      processorBrand : 'Intel',
      processorModel : 'i7',
      processorCores : '4',
      ramGeneration : 'ddr4',
      ramAmount : '16',
      storageType : 'ssd',
      storageAmount : '500',
      screenSize : '13',
      condition : 'new',
      url : 'http://asus.com'
    };

  }

}
