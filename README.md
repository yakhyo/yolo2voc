### Convert YOLO to Pascal VOC format or Pascal to YOLO format 

- Modify variables in `config.py` based on your dataset
- Run python `main.py --yolo2voc` to convert YOLO to VOC
- Run python `main.py --voc2yolo` to convert VOC to YOLO
- Run python `main.py --voc2yolo_a` to convert VOC to YOLO (absolute)

### Pascal VOC To YOLO 
`main.py --voc2yolo`
- `<object-class>` - integer number of object from `0` to `(classes-1)`
- `<x> <y> <width> <height>` - `float` values relative to width and height of image, it can be equal from `(0.0 to 1.0]`
- For example: `<x> = <absolute_x> / <image_width> or <height> = <absolute_height> / <image_height>`
- Attention: `<x> <y>` - are center of rectangle (are not top-left corner)

Let's say for `img1.jpg` you will be created `img1.txt` containing:
```
1 0.716797 0.395833 0.216406 0.147222
0 0.687109 0.379167 0.255469 0.158333
1 0.420312 0.395833 0.140625 0.166667
```
### Pascal VOC To YOLO Absolute

`main.py --voc2yolo`
- `<object-class>` - integer number of object from `0` to `(classes-1)`
- `<x_min> <y_min> <x_max> <y_max>` - `int` absolute values object coordinates 
- For example: `<object-class> <x_min> <y_min> <x_max> <y_max>`:
```
1 255 247 425 468
0 470 105 680 468
1 152 356 658 754
```
### Reference
1. [AlexeyAB](https://github.com/AlexeyAB/Yolo_mark/issues/60)
2. [Jahongir7174](https://github.com/jahongir7174/YOLO2VOC)