# Objectives

These are an outline of objectives for Foxtrot Upscaler v2. They are a rough list of technical descriptions that would show improvement of technical capability, turnaround-time, and overall efficiency in FTUv2.

*(this list is neither exhaustive nor final)*

* Upscaling shall be
    * Driven by a toggle-model mode
        * Multiple edge-finding modes are used during the core process of upscaling, each model specializing in it's own art-style (i.e. one mode for 2D, another for 3D)
    * Utilize memory, as opposed to flushing frames to disk, in order to sever dependence on disk as minimum-hardware-requirements
    * Utilize OpenCV image processing to modify image properties such as hue, sharpness, contrast, in real-time to the core upscaling process
* Art-Style Classifier shall be
    * Capable of classifying and distringuishing on a per-frame-basis the difference between an image drawn in 2D animation and an image drawn in 3D animation
