# Public Demo Script

Run the portable ultrasound demo:

```bash
python demo/portable-ultrasound/run_demo.py
```

Then inspect:

```bash
python -m json.tool demo/portable-ultrasound/artifacts_v0.2/receipt.json
sed -n '1,160p' demo/portable-ultrasound/artifacts_v0.2/report.md
```

Reviewer narration:

1. The demo uses synthetic metadata and synthetic manifest content.
2. The validator checks UDI-DICOM evidence consistency.
3. Device UID remains distinct from UDI-DI.
4. Registry evidence is supplied through offline fixtures by default.
5. The output is a review receipt and report, not a clinical, regulatory, or
   certification result.
