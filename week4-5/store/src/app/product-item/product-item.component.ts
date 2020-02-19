import {Component, OnChanges, OnInit, SimpleChanges} from '@angular/core';
import {ActivatedRoute} from '@angular/router';
import {map} from 'rxjs/operators';


@Component({
  selector: 'app-product-item',
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css']
})
export class ProductItemComponent implements OnInit {
  product: any;

  constructor(public activatedRoute: ActivatedRoute) {
  }

  ngOnInit() {
    this.product = window.history.state;
    console.log(this.product.product);
  }

  changeImage(id) {
    const main = document.getElementById('main') as HTMLImageElement;
    const need = document.getElementById(id) as HTMLImageElement;
    main.src = need.src;
  }

  Share() {
    window.open(this.product.product.link);
  }



}
