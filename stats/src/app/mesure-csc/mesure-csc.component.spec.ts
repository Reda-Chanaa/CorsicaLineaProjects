import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MesureCscComponent } from './mesure-csc.component';

describe('MesureCscComponent', () => {
  let component: MesureCscComponent;
  let fixture: ComponentFixture<MesureCscComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MesureCscComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(MesureCscComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
