import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MesureAlgComponent } from './mesure-alg.component';

describe('MesureAlgComponent', () => {
  let component: MesureAlgComponent;
  let fixture: ComponentFixture<MesureAlgComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MesureAlgComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(MesureAlgComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
