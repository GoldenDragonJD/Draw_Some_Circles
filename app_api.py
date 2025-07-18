# app_api.py
import flask
import json
import circle_tool
import io
import os

app = flask.Flask(__name__)


@app.route("/api/get_image", methods=["GET"])
def api_call():
    try:
        # Ensure the plot exists
        if not os.path.exists("circle_plot.png"):
            circle_tool.plot_the_circles()

        with open("circle_plot.png", "rb") as f:
            img_bytes = io.BytesIO(f.read())
        img_bytes.seek(0)
        return flask.send_file(img_bytes, mimetype="image/png")
    except Exception as e:
        return flask.jsonify({"error": str(e)}), 500


@app.route("/api/add_circle", methods=["POST"])
def add_circle():
    try:
        json_data = flask.request.get_json()

        # Validate input
        if not json_data or 'name' not in json_data:
            return flask.jsonify({"error": "Invalid input"}), 400

        # Ensure circle_data.json exists
        if not os.path.exists("circle_data.json"):
            with open("circle_data.json", "w") as f:
                json.dump({}, f)

        with open("circle_data.json", "r") as f:
            json_content = json.load(f)

        json_content[json_data["name"]] = json_data

        with open("circle_data.json", "w") as f:
            json.dump(json_content, f)

        circle_tool.plot_the_circles()
        return flask.jsonify({"result": "success"})
    except Exception as e:
        return flask.jsonify({"error": str(e)}), 500


@app.route("/api/remove_circle", methods=["POST"])
def remove_circle():
    try:
        json_data = flask.request.get_json()

        if not json_data or 'name' not in json_data:
            return flask.jsonify({"error": "Invalid input"}), 400

        if not os.path.exists("circle_data.json"):
            return flask.jsonify({"error": "No circles to remove"}), 404

        with open("circle_data.json", "r") as f:
            json_content = json.load(f)

        if json_data["name"] not in json_content:
            return flask.jsonify({"error": "Circle not found"}), 404

        del json_content[json_data["name"]]

        with open("circle_data.json", "w") as f:
            json.dump(json_content, f)

        circle_tool.plot_the_circles()
        return flask.jsonify({"result": "success"})
    except Exception as e:
        return flask.jsonify({"error": str(e)}), 500


@app.route("/api/get_circles", methods=["GET"])
def get_circles():
    try:
        if not os.path.exists("circle_data.json"):
            with open("circle_data.json", "w") as f:
                json.dump({}, f)
            return flask.jsonify({})

        with open("circle_data.json", "r") as f:
            data = json.load(f)
        return flask.jsonify(data)
    except Exception as e:
        return flask.jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    circle_tool.plot_the_circles()
    app.run(debug=True)
