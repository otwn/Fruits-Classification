<template>
  <div class="container">
    <div>
      <marquee direction="left" style="color:orangered;"
        ><h3>Fruit Classifier</h3></marquee
      >

      <form
        id="upload-form"
        action="{{ url_for('upload') }}"
        method="POST"
        enctype="multipart/form-data"
      >
        <div class="login card" style="color: orangered;">
          <pre>
  <h1 style="width: fit-content;color: orangered;">Upload Image To Classify<br> Fruit</h1>
  <strong>Choose Image:</strong>
  <input class="btn btn-primary btn-block btn-large" type="file" name="file" accept="image/*" multiple>
  <input type="submit" value="Predict!" class="btn btn-primary btn-block btn-large">
  </pre>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style>
.container {
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

::placeholder {
  color: rgb(13, 13, 14);
  opacity: 0.8; /* Firefox */
  font-weight: bold;
}
</style>
