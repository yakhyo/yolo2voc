from xml.etree import ElementTree
import os
import config


def voc2yolo_absolute(xml_file):
    in_file = open(f'{config.xml_dir}/{xml_file}')
    tree = ElementTree.parse(in_file)

    class_exists = False
    for obj in tree.findall('object'):
        name = obj.find('name').text
        if name in config.names:
            class_exists = True

    if class_exists:
        out_file = open(f'{config.label_dir}/{xml_file[:-4]}.txt', 'w')
        for obj in tree.findall('object'):
            xml_box = obj.find('bndbox')
            x_min = int(xml_box.find('xmin').text)
            y_min = int(xml_box.find('ymin').text)
            x_max = int(xml_box.find('xmax').text)
            y_max = int(xml_box.find('ymax').text)

            bbox = [x_min, y_min, x_max, y_max]
            cls_id = config.names.index(obj.find('name').text)
            out_file.write(str(cls_id) + " " + " ".join([str(f'{b}') for b in bbox]) + '\n')
        out_file.close()


if __name__ == '__main__':
    xml_files = [name for name in os.listdir(config.xml_dir) if name.endswith('.xml')]
    for i in xml_files[:50]:
        voc2yolo_absolute(i)



