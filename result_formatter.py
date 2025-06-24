def format_results(indices, df):
    seen_titles = set()
    results = []
    for idx in indices:
        title = df.iloc[idx]["TITLE"].strip()
        if title in seen_titles:
            continue
        seen_titles.add(title)
        summary = df.iloc[idx]["DESCRIPTION"][:300].replace("\n", " ")
        results.append({
            "title": title,
            "date": df.iloc[idx]["MOD_DATE"],
            "source": df.iloc[idx]["SOURCE_NAME"],
            "summary": summary
        })
        if len(results) >= 5:
            break
    return results