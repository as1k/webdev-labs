import { Injectable } from '@angular/core';
import {Observable, of} from 'rxjs';
import { products } from './products';

@Injectable({
  providedIn: 'root'
})
export class ProductService {

  constructor() { }

  getProduct(id: number): Observable<any> {
    return of(products.find(product => product.id === id));
  }

  getProducts(): Observable<any> {
    return of(products);
  }

  getProductsByCategoryId(id: number): Observable<any> {
    return of(products.filter(product => product.category_id === id));
  }
}
