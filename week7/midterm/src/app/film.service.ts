import { Injectable } from '@angular/core';
import { Film } from './film';
import { FILMS } from './mock-films';
import { Observable, of } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class FilmService {

  constructor() { }

  getFilms(): Observable<Film[]> {
    return of(FILMS);
  }
  getFilm(id: number): Observable<Film> {
    return of(FILMS.find(film => film.id === id));
  }

  films = FILMS;

  incrViewCount(id): void {
    this.films.find(film => film.id === id).view_count = ((FILMS.find(film => film.id === id).view_count)+1);
  }

}

