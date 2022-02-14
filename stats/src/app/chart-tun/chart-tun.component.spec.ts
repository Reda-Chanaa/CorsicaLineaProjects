import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ChartTunComponent } from './chart-tun.component';

describe('ChartTunComponent', () => {
  let component: ChartTunComponent;
  let fixture: ComponentFixture<ChartTunComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ChartTunComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ChartTunComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
