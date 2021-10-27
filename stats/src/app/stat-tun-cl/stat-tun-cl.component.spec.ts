import { ComponentFixture, TestBed } from '@angular/core/testing';

import { StatTunClComponent } from './stat-tun-cl.component';

describe('StatTunClComponent', () => {
  let component: StatTunClComponent;
  let fixture: ComponentFixture<StatTunClComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ StatTunClComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(StatTunClComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
