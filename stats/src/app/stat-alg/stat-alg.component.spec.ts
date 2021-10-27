import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StatAlgComponent } from './stat-alg.component';

describe('StatAlgComponent', () => {
  let component: StatAlgComponent;
  let fixture: ComponentFixture<StatAlgComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ StatAlgComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(StatAlgComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
