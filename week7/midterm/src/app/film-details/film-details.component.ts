import { Component, OnInit, Input } from '@angular/core';

import { Film } from '../film';
import { FILMS } from '../mock-films';

import { FilmService } from '../film.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-film-details',
  templateUrl: './film-details.component.html',
  styleUrls: ['./film-details.component.css']
})
export class FilmDetailsComponent implements OnInit {
  @Input() film: Film;
  constructor(private route: ActivatedRoute,
              private filmService: FilmService) { }

  ngOnInit(): void {
    this.getFilm();
  }

  getFilm(): void {
    const id = +this.route.snapshot.paramMap.get('id');
    this.filmService.getFilm(id)
      .subscribe(film => this.film = film);
  }
}
