import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ConcoTunComponent } from './conco-tun.component';

describe('ConcoTunComponent', () => {
  let component: ConcoTunComponent;
  let fixture: ComponentFixture<ConcoTunComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ConcoTunComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ConcoTunComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
