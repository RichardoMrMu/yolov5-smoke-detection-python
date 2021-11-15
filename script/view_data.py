import os 
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
# watch txt files' labels
def get_label(label_pathes):
    labels = {}
    for path in label_pathes:
        with open(path,'r') as f:
            datas = f.readlines()
            for data in datas:
                label = data.split(" ")[0]
                if label in labels.keys():
                    labels[label] += 1
                else :
                    labels[label] = 1
    print(labels)

# parse xml files 
def parsexml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    filename = root.find('filename').text
    boxes = []
    classnames = []
    for obj in root.findall('object'):
        name = obj.find('name').text
        bndbox = obj.find('bndbox')
        xmin = bndbox.find('xmin').text
        ymin = bndbox.find('ymin').text
        xmax = bndbox.find('xmax').text
        ymax = bndbox.find('ymax').text
        if int(xmin) >= int(xmax) or int(ymin) >= int(ymax):
            continue
        boxes.append([int(xmin), int(ymin), int(xmax), int(ymax)])
        classnames.append(name)
    return classnames, boxes


# watch  xml files' labels 
def get_xml_labels(xml_pathes):
    labels_name = {}
    for xml_file in xml_pathes:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        filename = root.find('filename').text
        for obj in root.findall('object'):
            name = obj.find('name').text
            if name in labels_name.keys():
                labels_name[name] += 1
            else :
                labels_name[name] = 1
    print(labels_name)


def main():
    # get path list 
    path = "./labels"
    label_pathes = os.listdir(path)
    label_pathes = [os.path.join(path,i) for i in label_pathes]
    get_label(label_pathes)

def main2():
    # see xml labels 
    path = "./Annotations"
    label_pathes = os.listdir(path)
    label_pathes = [os.path.join(path,i) for i in label_pathes]
    get_xml_labels(label_pathes)

if __name__ == "__main__":
    # main()
    main2()