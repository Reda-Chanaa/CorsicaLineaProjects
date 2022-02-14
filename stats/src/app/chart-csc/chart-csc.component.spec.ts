import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ChartCscComponent } from './chart-csc.component';

describe('ChartCscComponent', () => {
  let component: ChartCscComponent;
  let fixture: ComponentFixture<ChartCscComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ChartCscComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ChartCscComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
