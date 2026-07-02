from library_service import LibraryService
import pytest

def test_calculate_tax():
    service = LibraryService()
    assert service.calculate_total(100) == 118

def test_negative_amount():
    service = LibraryService()
    with pytest.raises(ValueError):
        service.calculate_total(-100)

def test_daily_limit():
    service = LibraryService()
    with pytest.raises(ValueError):
        service.process_payment(15000)