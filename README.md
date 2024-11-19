## Convert YOLO to Pascal VOC format or Pascal to YOLO format

![GitHub License](https://img.shields.io/github/license/yakhyo/yolo2voc) 
[![GitHub Repo stars](https://img.shields.io/github/stars/yakhyo/yolo2voc)](https://github.com/yakhyo/yolo2voc/stargazers)
[![GitHub Repository](https://img.shields.io/badge/GitHub-Repository-blue?logo=github)](https://github.com/yakhyo/yolo2voc)

### Usage:

```
git clone https://github.com/yakhyo/yolo2voc.git
cd yolo2voc
pip install -r requirements.txt
```

- Modify variables in `config.py` based according to your dataset
- Run python `main.py --yolo2voc` to convert **YOLO** to **VOC**
- Run python `main.py --voc2yolo` to convert **VOC** to **YOLO**
- Run python `main.py --voc2yolo_a` to convert **VOC** to **YOLO** (absolute)

### Pascal VOC To YOLO

`main.py --voc2yolo`

- `<object-class>` - integer number of object from `0` to `(classes-1)`
- `<x> <y> <width> <height>` - `float` values relative to width and height of an image, it can be within range
  of `(0.0 to 1.0]`
- For example: `<x> = <absolute_x> / <image_width> or <height> = <absolute_height> / <image_height>`
- Attention: `<x> <y>` - are center of rectangle (are not top-left corner)

<div align="center">
    <p><code>zidane.jpg</code></p>
    <img src="assets/zidane.jpg" height="400px" alt="downloaded from ultralytics">
</div>

The label file corresponding to the above image contains 2 persons (class 0) and a tie (class 27):

`<object-class> <x> <y> <width> <height>`
<div align="center">
    <img src="assets/zidane_txt.jpg", height="200px" alt="downloaded from ultralytics">
</div>

### Pascal VOC To YOLO Absolute

`main.py --voc2yolo_a`

- `<object-class>` - integer number of object from `0` to `(classes-1)`
- `<x_min> <y_min> <x_max> <y_max>` - `int` absolute values object coordinates
- For example: `<object-class> <x_min> <y_min> <x_max> <y_max>`:

```
1 255 247 425 468
0 470 105 680 468
1 152 356 658 754
```

### Reference

1. https://github.com/AlexeyAB/Yolo_mark/issues/60
2. https://github.com/jahongir7174/YOLO2VOC
