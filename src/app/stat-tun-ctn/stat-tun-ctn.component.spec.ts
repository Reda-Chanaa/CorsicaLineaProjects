import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StatTunCtnComponent } from './stat-tun-ctn.component';

describe('StatTunCtnComponent', () => {
  let component: StatTunCtnComponent;
  let fixture: ComponentFixture<StatTunCtnComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ StatTunCtnComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(StatTunCtnComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
