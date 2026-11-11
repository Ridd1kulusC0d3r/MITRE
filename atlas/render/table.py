"""data/ecosystem.csv"""
import csv
import io

CSV_FIELDS = ["id", "name", "url", "origin", "owner_type", "layer", "domains", "priority",
              "status", "version", "formats", "relations", "purpose", "output", "notes",
              "license_api", "archived", "pushed_at", "reviewed_on", "verification"]


def render(d):
    out = io.StringIO()
    wr = csv.DictWriter(out, fieldnames=CSV_FIELDS, extrasaction="ignore", lineterminator="\n")
    wr.writeheader()
    for e in d["entries"]:
        row = dict(e)
        for k in ("domains", "formats", "relations"):
            row[k] = ";".join(e.get(k, []))
        wr.writerow(row)
    return out.getvalue()
