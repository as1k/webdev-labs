import { Component } from '@angular/core';

import { products } from '../products';
@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent{
  products = products;

  share(product) {
    const url: string = window.location.href;
    window.alert(`The product ${ product.name } has been shared!`);
    window.open(`https://telegram.me/share/url?url=${ product.link }&text=Hey, check out this cool ${ product.name }`);
  }

  onNotify(product) {
    window.alert(`You will be notified when ${product.name} goes on sale`);
  }
}


/*
Copyright Google LLC. All Rights Reserved.
Use of this source code is governed by an MIT-style license that
can be found in the LICENSE file at http://angular.io/license
*/
