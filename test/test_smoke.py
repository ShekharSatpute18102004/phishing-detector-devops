from phishing_detector import is_phishing_url_rule

def test_basic_rule():
    suspicious, reason = is_phishing_url_rule("http://test.com", return_reason=True)
    assert suspicious is True
    assert "HTTPS" in reason or "http" in reason.lower()

def test_safe_url():
    suspicious, reason = is_phishing_url_rule("https://example.com", return_reason=True)
    assert suspicious is False
