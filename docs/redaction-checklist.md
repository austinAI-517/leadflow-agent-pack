# Redaction Checklist

Use this before pasting lead samples into AI tools, public issues, chats, or support messages.

## Never Paste

- Real customer names.
- Personal email addresses.
- Phone numbers.
- Street addresses.
- CRM account IDs.
- API keys.
- Auth tokens.
- Session cookies.
- Private `.env` values.
- Full unrelated CRM exports.
- Payment, health, legal, or other sensitive personal details.

## Replace With Safe Labels

```text
<REDACTED_NAME>
<REDACTED_EMAIL>
<REDACTED_PHONE>
<REDACTED_ADDRESS>
<REDACTED_TOKEN>
<PRIVATE_CRM_ID>
<PRIVATE_ACCOUNT>
```

## Usually Safe To Include

- Lead source category, such as website form, ad lead, referral, or CSV export.
- General timeline, such as this week, next month, or no rush.
- General budget band, if it is not tied to an identifiable person.
- Redacted need description.
- Column names without private values.

## Redaction Note

Add this note to any sample:

```text
Redaction note:
I removed names, emails, phone numbers, addresses, tokens, customer IDs, and unrelated private fields. Values shown here are sample-safe or anonymized.
```
