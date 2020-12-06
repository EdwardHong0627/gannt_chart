import os
import sys


class GanntChart(object):
    def __init__(self, num_of_machine: int, total_length: int, scale: int):
        self.height = num_of_machine * 80 + 80
        self.width = total_length * scale
        self.scale = scale
        self.num_of_machine = num_of_machine
        self.num_of_jobs = 0
        self.font_size = 20
        self.svg = "<svg width=\"" + str(self.width + 100) + "\" height=\"" + str(
            self.height + 100) + "\" xmlns=\"http://www.w3.org/2000/svg\" xmlns:xlink=\"http://www.w3.org/1999/xlink\">\n"
        self.svg += "<line fill=\"none\" stroke=\"#000000\" stroke-width=\"3\"  x1=\"40\" y1=\"10\" x2=\"40\" y2=\"" + str(
            self.height) + "\" />\n"
        for i in range(1, self.num_of_machine + 1):
            self.svg += "<text fill=\"#000000\" stroke=\"#000000\" stroke-width=\"0\" font-size=\"20\" font-family=\"serif\" " + \
                        "text-anchor=\"left\" xml:space=\"preserve\" font-weight=\"bold\"  x=\"5\" y=\"" + str(
                60 + (i - 1) * 80) + "\" >M" + str(i) + "</text>\n\n"

        for i in range(10, self.width, 10):
            self.svg += "<text fill=\"#000000\" stroke=\"#000000\" stroke-width=\"0\" font-size=\"14\" font-family=\"serif\" " + \
                        "text-anchor=\"center\" xml:space=\"preserve\" font-weight=\"bold\"  x=\"" + str(
                (i * self.scale) + 40) + "\" y=\"" + str(self.height + 25) + "\" >" + str(i) + "</text>\n\n"
            self.svg += "<line fill=\"none\" stroke=\"#000000\" stroke-width=\"3\"  x1=\"" + str(
                (i * self.scale) + 40) + "\" y1=\"" + str(self.height - 5) + "\" x2=\"" + str(
                (i * self.scale) + 40) + "\" y2=\"" + str(
                self.height) + "\" id=\"\"/>\n"
        self.svg += "<line fill=\"none\" stroke=\"#000000\" stroke-width=\"3\"  x1=\"40\" y1=\"" + str(
            self.height) + "\" x2=\"" + str(self.width + 100) + "\" y2=\"" + str(self.height) + "\" id=\"\"/>\n"

    def add_job(self, job_name, machine: str, starting_time: int, processing_time: int):
        self.svg += "<rect width=\"" + str(
            self.scale * processing_time) + "\" height=\"60\" style=\"fill:#FFFFFF;fill-opacity=1;stroke-width:1;\"  stroke=\"#000000 \" x=\"" \
                    + str(starting_time * self.scale + 40) + "\" y=\"" + str(25 + (machine - 1) * 80) + "\"  />\n\n"
        self.svg += "<text fill=\"#000000\" stroke=\"#000000\" stroke-width=\"0\" font-size=\"" + str(
            self.font_size) + "\" font-family=\"serif\" " + \
                    "text-anchor=\"center\" xml:space=\"preserve\" font-weight=\"bold\"  x=\"" + str(
            (2 * starting_time * self.scale + processing_time * self.scale) / 2 + 35) \
                    + "\" y=\"" + str(60 + (machine - 1) * 80) + "\" >" + job_name + " </text>\n\n"
        self.svg += "<text fill=\"#000000\" stroke=\"#000000\" stroke-width=\"0\" font-size=\"" + str(
            self.font_size) + "\" font-family=\"serif\" " + \
                    "text-anchor=\"center\" xml:space=\"preserve\" font-weight=\"bold\"  x=\"" + str(
            (starting_time * self.scale + processing_time * self.scale + 40)) + "\" y=\"" \
                    + str(25 + (machine - 1) * 80 + 75) + "\" >" + str(starting_time + processing_time) + "</text>\n\n"

    def save_to_file(self, file_name: str):
        self.svg += "</svg>"
        ow = open(file_name + ".svg", 'w')
        ow.write(self.svg)
        ow.close()

    def set_font_size(self, font_size: int):
        self.font_size = font_size
