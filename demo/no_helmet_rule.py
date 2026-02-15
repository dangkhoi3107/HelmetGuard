"""
NO_HELMET rule skeleton (WIP)

Idea:
- Detect person + helmet (after you fine-tune your model).
- For each person bbox, define head area = top 1/3 of the person bbox.
- If no helmet bbox overlaps head area -> NO_HELMET.
"""

def mark_no_helmet(person_boxes, helmet_boxes, iou_thresh=0.05):
    # person_boxes: list of (x1,y1,x2,y2)
    # helmet_boxes: list of (x1,y1,x2,y2)
    results = []
    for (x1,y1,x2,y2) in person_boxes:
        hx1, hy1 = x1, y1
        hx2, hy2 = x2, y1 + (y2 - y1) / 3.0  # head area
        # TODO: compute overlap with helmets and set has_helmet
        has_helmet = False
        results.append({"person": (x1,y1,x2,y2), "has_helmet": has_helmet})
    return results
