import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ConcoAlgComponent } from './conco-alg.component';

describe('ConcoAlgComponent', () => {
  let component: ConcoAlgComponent;
  let fixture: ComponentFixture<ConcoAlgComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ConcoAlgComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ConcoAlgComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
