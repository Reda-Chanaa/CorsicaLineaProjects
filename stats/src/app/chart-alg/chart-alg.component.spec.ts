import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ChartAlgComponent } from './chart-alg.component';

describe('ChartAlgComponent', () => {
  let component: ChartAlgComponent;
  let fixture: ComponentFixture<ChartAlgComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ChartAlgComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ChartAlgComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
